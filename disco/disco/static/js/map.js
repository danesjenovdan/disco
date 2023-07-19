(async () => {
  const map = L.map("map").setView([46.0563472, 14.5330039], 14);

  var myIcon = L.icon({
    iconUrl: __MARKER_STATIC_URL__,
    iconSize: [50, 70],
    iconAnchor: [25, 70],
  });

  // var marker = L.marker([46.0563472,14.5330039], {icon: myIcon}).addTo(map);

  var cityHotel = L.marker([46.0544587, 14.5080861], { icon: myIcon })
    .addTo(map)
    .bindPopup("City Hotel Ljubljana: Dalmatinova ulica 15");

  var hotelSlon = L.marker([46.0531182, 14.5037718], { icon: myIcon })
    .addTo(map)
    .bindPopup("Slon: Slovenska cesta 34");

  var spanskiBorci = L.marker([46.0569837, 14.5355788], { icon: myIcon })
    .addTo(map)
    .bindPopup("Španski borci: Zaloška cesta 61");

  var dijaskiDomTabor = L.marker([46.0543522, 14.5130375], { icon: myIcon })
    .addTo(map)
    .bindPopup("Dijaški dom Tabor: Kotnikova ulica 4");

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);
})();
