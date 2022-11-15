// Initialize and add the map
function initMap() {
    // Locations
    const coruna = {lat: 43.365, lng: -8.410}
    const madrid = {lat: 40.416667, lng: -3.7025}
    const barcelona = {lat: 41.3825, lng: 2.176944}


    // The map, centered at Crouna
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: coruna,
    });

    // Markers
    // Coruña
    const markerCoruna = new google.maps.Marker({position: coruna, map: map});
    // Madrid
    const markerMadrid = new google.maps.Marker({position: madrid, map: map})
    // Barcelona
    const markerBarcelona = new google.maps.Marker({position: barcelona, map: map})
  }
  
  window.initMap = initMap;