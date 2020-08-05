var ui;
var dbUsuarios;

initializeFirebaseRealtime();
initializeFirebaseUI();

function initializeFirebaseRealtime() {
    const firebaseConfig = {
        apiKey: "AIzaSyDaOMb9NqdH2MBOo1s3XDTtK3Jf52iPd5A",
        authDomain: "aruna-security.firebaseapp.com",
        databaseURL: "https://aruna-security.firebaseio.com",
        projectId: "aruna-security",
        storageBucket: "aruna-security.appspot.com",
        messagingSenderId: "508716484340",
        appId: "1:508716484340:web:0dd287aba4b83c1a39c0a1",
        measurementId: "G-9ZYN4E30GR"
    };
    try {
        firebase.initializeApp(firebaseConfig);
        dbUsuarios = firebase.database().ref("usuarios");
    } catch (e) {
        console.error("Error de inicialización de Firebase", e.stack)
    }
}

function initializeFirebaseUI() {
    uiConfig = {
        callbacks: {
            signInSuccessWithAuthResult: function (currentUser, credential, redirectUrl) {
                //setAuthUser(currentUser, credential, redirectUrl);
                return false;
            },
            uiShown: function () {
                //document.getElementById('loader').style.display = 'none';
            }
        },
        signInSuccessUrl: '<url-to-redirect-to-on-success>',
        signInOptions: [
            firebase.auth.GoogleAuthProvider.PROVIDER_ID,
            firebase.auth.EmailAuthProvider.PROVIDER_ID,
            //firebase.auth.FacebookAuthProvider.PROVIDER_ID,
            //firebase.auth.TwitterAuthProvider.PROVIDER_ID,
        ],
        tosUrl: 'tos.html',
        privacyPolicyUrl: function () {
            window.location.assign('tos.html');
        }
    };
    ui = new firebaseui.auth.AuthUI(firebase.auth());
    ui.start('#firebaseui-auth-container', uiConfig);
}

function loadUserFromFB(userId) {
    return new Promise((resolve, reject) => {
        dbUsuarios.orderByChild("email").equalTo(userId).on("value", user => {
            if (user.val()) {
                resolve(user.val());
            } else {
                resolve(null);
            }
        });
    });
}

