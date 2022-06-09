const subject = document.getElementById("subject");
const toeic_opic = document.getElementById("toeic_opic");
const select_english = document.getElementById("select-english");

function onSelector(event) {
  if (event.target.value == "toeic") {
    const toeic = document.createElement("select");
    toeic.name = "toeic";
    toeic.id = "toeic";
    const opt1 = document.createElement("option");
    opt1.value = "LV8";
    opt1.text = "LV 8";
    const opt2 = document.createElement("option");
    opt2.value = "LV7";
    opt2.text = "LV 7";
    const opt3 = document.createElement("option");
    opt3.value = "LV6";
    opt3.text = "LV 6";
    const opt4 = document.createElement("option");
    opt4.value = "LV5";
    opt4.text = "LV 5";
    toeic.add(opt1, null);
    toeic.add(opt2, null);
    toeic.add(opt3, null);
    toeic.add(opt4, null);
    select_english.appendChild(toeic);
    const opic = document.getElementById("opic");
    if (opic) {
      opic.remove();
    }
  } else if (event.target.value == "opic") {
    const opic = document.createElement("select");
    opic.name = "opic";
    opic.id = "opic";
    const opt1 = document.createElement("option");
    opt1.value = "AL";
    opt1.text = "AL";
    const opt2 = document.createElement("option");
    opt2.value = "IH";
    opt2.text = "IH";
    const opt3 = document.createElement("option");
    opt3.value = "IM3";
    opt3.text = "IM3";
    const opt4 = document.createElement("option");
    opt4.value = "IM2";
    opt4.text = "IM2";
    const opt5 = document.createElement("option");
    opt5.value = "IM1";
    opt5.text = "IM1";
    const opt6 = document.createElement("option");
    opt6.value = "IL";
    opt6.text = "IL";
    opic.add(opt1, null);
    opic.add(opt2, null);
    opic.add(opt3, null);
    opic.add(opt4, null);
    opic.add(opt5, null);
    opic.add(opt6, null);
    select_english.appendChild(opic);
    const toeic = document.getElementById("toeic");
    if (toeic) {
      toeic.remove();
    }
  } else {
    const opic = document.getElementById("opic");
    const toeic = document.getElementById("toeic");
    if (opic) {
      opic.remove();
    }
    if (toeic) {
      toeic.remove();
    }
  }
}
subject.addEventListener("change", onSelector);
