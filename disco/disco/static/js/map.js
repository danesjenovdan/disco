(async () => {
  const map = L.map("map").setView([46.0563472, 14.5330039], 14);

  var myIcon = L.icon({
    iconUrl: __MARKER_STATIC_URL__,
    iconSize: [50, 70],
    iconAnchor: [25, 70],
  });

  var cityHotel = L.marker([46.05376568722064, 14.508026597389362], { icon: myIcon })
    .addTo(map)
    .bindPopup("City Hotel: Dalmatinova ulica 15");

  var hotelSlon = L.marker([46.05261256932129, 14.50374768122139], { icon: myIcon })
    .addTo(map)
    .bindPopup("Best Western Premier Hotel Slon: Slovenska cesta 34");

  var spanskiBorci = L.marker([46.056363991241454, 14.535515637904632], { icon: myIcon })
    .addTo(map)
    .bindPopup("Španski borci: Zaloška cesta 61");

  var dijaskiDomTabor = L.marker([46.05350706793265, 14.513555725245713], { icon: myIcon })
    .addTo(map)
    .bindPopup("Dijaški dom Tabor: Kotnikova ulica 4");

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);
})();
