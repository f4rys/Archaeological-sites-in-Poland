require.config({
    paths: {
        "leaflet": "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet",
        "google-mutant": "https://unpkg.com/leaflet.gridlayer.googlemutant@latest/dist/Leaflet.GoogleMutant"
    },
  });

define(['leaflet', 'leaflet.wms', 'google-mutant'],

function(L, wms) {

    var overlayMap = createMap('overlay-map', false);

    function createMap(div) {

        var map = L.map(div);
        map.setView([50.574283, 19.722619], 6);

        var roadmap = L.gridLayer.googleMutant({
            type: 'roadmap'
        });

        var satellite = L.gridLayer.googleMutant({
            type: 'satellite'
        });

        var terrain = L.gridLayer.googleMutant({
            type: 'terrain'
        });

        var hybrid = L.gridLayer.googleMutant({
            type: 'hybrid'
        });

        var basemaps = {
            'Google Roadmap' : roadmap.addTo(map),
            'Google Satellite' : satellite,
            'Google Terrain' : terrain,
            'Google Hybrid' : hybrid
        };

        var source = wms.source(
            "https://usluga.zabytek.gov.pl/INSPIRE_AMD/service.svc/get?",
            {
                "format": "image/png",
                "transparent": "true",
            }        
        ).getLayer("Archaeological_Monuments").addTo(map);

        L.control.layers(basemaps).addTo(map);

        return map;
    }

return overlayMap
});

