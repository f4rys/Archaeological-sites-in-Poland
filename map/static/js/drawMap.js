require.config({
    paths: {
      "leaflet": "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet",
      "leaflet-providers": "https://cdn.jsdelivr.net/npm/leaflet-providers@latest/leaflet-providers"
    },
  });
  
  define(['leaflet', 'leaflet.wms', 'leaflet-providers'], function(L, wms, L_P) {
  
    var overlayMap = createMap('overlay-map', false);
  
    function createMap(div) {
  
      var map = L.map(div);
      map.setView([50.574283, 19.722619], 6);
  
      var roadmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      });
    
      var satellite = L.tileLayer.provider('Esri.WorldImagery');
      var topographic = L.tileLayer.provider('OpenTopoMap');
  
      var basemaps = {
        'Roadmap': roadmap,
        'Satellite': satellite,
        'Topographic': topographic,
      };
  
      roadmap.addTo(map);
  
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
  
    return overlayMap;
  });
  