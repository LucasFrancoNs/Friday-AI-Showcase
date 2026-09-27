const agents = [
  ["RESEARCHER", "standby", "read-only intelligence"],
  ["DEVELOPER", "sandbox", "staged workspace only"],
  ["TESTER", "ready", "validation gate"],
  ["REVIEWER", "ready", "final evidence review"],
];

const logLines = [
  "policy.engine // no privilege escalation",
  "defender // integrity baseline verified",
  "router // lazy capabilities enabled",
  "sandbox // promotion requires separate gate",
  "context // bounded session policy active",
];

const $ = (id) => document.getElementById(id);
$("agents").innerHTML = agents.map(([name, status, desc]) => `<div class="agent"><strong>${name}</strong><b>${status.toUpperCase()}</b><small>${desc}</small></div>`).join("");
$("eventLog").innerHTML = logLines.map((line, i) => `<div class="event"><b>${String(i + 1).padStart(2,"0")}</b> ${line}</div>`).join("");

function tick() {
  const now = new Date();
  $("clock").textContent = now.toLocaleTimeString([], {hour12:false});
  const t = now.getSeconds();
  const cpu = 18 + Math.round((Math.sin(t / 5) + 1) * 8);
  const ram = 37 + Math.round((Math.cos(t / 7) + 1) * 4);
  $("cpu").style.width = `${cpu}%`;
  $("ram").style.width = `${ram}%`;
  $("cpuText").textContent = `${cpu}%`;
  $("ramText").textContent = `${ram}%`;
  $("coreValue").textContent = (97.1 + (Math.sin(t / 8) + 1) * .22).toFixed(1);
}

tick();
setInterval(tick, 1000);
