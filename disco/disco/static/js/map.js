(async () => {
  const map = L.map('map').setView([46.0563472,14.5330039], 13);

  var myIcon = L.icon({
    iconUrl: '/static/img/location-pin.png',
    iconSize: [50, 70],
    iconAnchor: [25, 70],
  });

  var marker = L.marker([46.0563472,14.5330039], {icon: myIcon}).addTo(map);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

})();
