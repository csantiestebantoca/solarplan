var myurl = "";
var app = angular.module("Administracion", []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{!');
    $interpolateProvider.endSymbol('!}');
});

app.controller("ControladorPrincipal", function ($scope) {

    $scope.initialization = () => {
        $scope.authUser = null;
        listenUserStatus();
        $scope.initialyzeSCADA();
        $scope.showMenu = false;
        $scope.plantName = "";
        $scope.selectedPlant = null;
        setPlansMap();
    };

    // #region USER LOGIN

    $scope.selectPlan = (plantName) => {
        $scope.showMenu = true;
        document.getElementById("plantName").innerHTML = plantName;
    }

    listenUserStatus = () => {
        firebase.auth().onAuthStateChanged(user => {
            if (user) {
                loadUserData(user);
            } else {
                $scope.authUser = null;
            }
        });
    };

    loadUserData = (user) => {
        loadUserFromFB(user.email).then(userData => {
            if (userData) {
                $scope.authUser = user;
                let key = Object.keys(userData)[0];
                $scope.authUser["role"] = userData[key].role;
                document.getElementById("userName").innerHTML = $scope.authUser.displayName.split(" ")[0];
                $scope.$apply();
            } else {
                $scope.logout();
                alert("Credenciales incorrectas, por favor vuelva a intentarlo!");
            }
        });
    }

    $scope.logout = () => {
        firebase.auth().signOut().then(function () {
            $scope.authUser = null;
            ui.start("#firebaseui-auth-container", uiConfig);
            // location.href = "{{=URL('default', 'index')}}";
            $scope.$apply();
        });
    };

    // #endregion USER LOGIN

    // #region SCADA

    $scope.initialyzeSCADA = () => {
        $scope.switch1 = true;
        $scope.switch2 = true;
        $scope.switch3 = true;
        $scope.switch4 = true;
        $scope.switch5 = true;
    }

    // #endregion SCADA

    //#region PLANTS

    $scope.plants = [
        { "id": "1", "name": "BOUJDOUR", "lat": "26.16", "long": "-14.36", "location": "Africa/Casablanca", "tracker_width": "3.93", "tracker_pitch": "15", "loss": "0.015", "inverter_capacity": "1164" },
        { "id": "3", "name": "LAAYOUNE", "lat": "26.99", "long": "-12.94", "location": "Africa/Casablanca", "tracker_width": "3.93", "tracker_pitch": "15", "loss": "0.015", "inverter_capacity": "1165" },
        { "id": "4", "name": "ALCOM", "lat": "24.4", "long": "32.75", "location": "Africa/Casablanca", "tracker_width": "3.03", "tracker_pitch": "6.15", "loss": "0.013", "inverter_capacity": "1500" },
        { "id": "6", "name": "BENBAN", "lat": "24.4", "long": "32.75", "location": "Africa/Cairo", "tracker_width": "3.03", "tracker_pitch": "6", "loss": "0.013", "inverter_capacity": "1500" },
        { "id": "7", "name": "OUARZAZATE", "lat": "31.02", "long": "-6.83", "location": "Africa/Casablanca", "tracker_width": "3.93", "tracker_pitch": "10", "loss": "0.015", "inverter_capacity": "1165" },
        { "id": "8", "name": "TK", "lat": "24.383", "long": "32.733", "location": "Africa/Cairo", "tracker_width": "3.03", "tracker_pitch": "7", "loss": "0.013", "inverter_capacity": "1500" },
        { "id": "9", "name": "VIETNAM", "lat": "11.31", "long": "108.75", "location": "Asia/Ho_Chi_Minh", "tracker_width": "5.902", "tracker_pitch": "7.962", "loss": "0.012", "inverter_capacity": "3125" }
    ];

    $scope.selectPlant = (plantId) => {
        for (let i = 0; i < $scope.plants.length; i++) {
            if ($scope.plants[i].id == plantId) {
                $scope.selectedPlant = $scope.plants[i];
            }
        }
        window.scrollTo(0, 0);
    }

    //#endregion PLANTS

    //#region MAPS

    setPlansMap = () => {

        var mymap = L.map('mapid').setView([30, 0], 1.5);

        var t = L.terminator();
        t.addTo(mymap);
        setInterval(function () {
            updateTerminator(t)
        }, 500);

        function updateTerminator(t) {
            t.setTime();
        }

        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
            maxZoom: 18,
            minZoom: 2,
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            id: 'mapbox/streets-v11',
            tileSize: 512,
            zoomOffset: -1
        }).addTo(mymap);

        var greenIcon = L.icon({
            iconUrl: 'leaf-green.png',
            shadowUrl: 'leaf-shadow.png',

            iconSize: [38, 95], // size of the icon
            shadowSize: [50, 64], // size of the shadow
            iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
            shadowAnchor: [4, 62],  // the same for the shadow
            popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
        });

        let estiloPopup = {
            'color': 'black !important',
            'backgrount-color': 'blue !important'
        };

        let iconoBase = L.Icon.extend({
            options: {
                iconSize: [20 + 2 * (mymap.getZoom()), 20 + 2 * (mymap.getZoom())]
            }
        });

        // let solarIcon = new iconoBase({ iconUrl: "{{=URL('static', 'images/solarpanel1.png')}}" });
        // let windIcon = new iconoBase({ iconUrl: "{{=URL('static', 'images/windpower1.png')}}" });
        let solarIcon = new iconoBase({ iconUrl: "solarplants/static/images/solarpanel1.png" });
        let windIcon = new iconoBase({ iconUrl: "solarplants/static/images/windpower1.png" });
        let markersArray = [];
        let plants = $scope.plants;

        for (let i = 0; i < plants.length; i++) {
            let m = L.marker([plants[i].lat, plants[i].long], { icon: solarIcon }).bindPopup(`<p><b>${plants[i].name}</b></p><p>Wind Farm</p>`, estiloPopup).addTo(mymap);
            markersArray.push(m);
        }

        mymap.on('zoomend', function () {});
    }

    //#endregion MAPS

    convertDashToDot = (input) => {
        return input.replace(/\-/g, ".");
    }

    convertDotToDash = (input) => {
        return input.replace(/\./g, "-");
    }

});
