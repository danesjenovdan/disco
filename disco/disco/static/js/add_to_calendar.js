import { atcb_action } from "https://cdn.jsdelivr.net/npm/add-to-calendar-button@2.2.9/+esm";

const button = document.querySelector("#add-to-calendar");

const config = {
  name: "DISCO Slovenia - Digital Sovereignty Conference",
  description: "Digital Sovereignty Conference[br][url]https://disco.si[/url]",
  location: "Ljubljana, Slovenia",
  startDate: "2023-10-24",
  endDate: "2023-10-26",
  timeZone: "Europe/Ljubljana",
  organizer: "Danes je nov dan|vsi@danesjenovdan.si",
  uid: "37dcc428-965a-4d5a-b964-e39ca3742de9",
  options: [
    "Apple",
    "Google",
    "iCal",
    "Microsoft365",
    "MicrosoftTeams",
    "Outlook.com",
    "Yahoo",
  ],
};

button.addEventListener("click", () => atcb_action(config, button));
