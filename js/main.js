// Icons (Lucide محلي)
lucide.createIcons();

// Contact form -> Formspree (AJAX)
const form = document.getElementById("contact-form");
const statusEl = document.getElementById("form-status");
const label = document.getElementById("send-label");

form.addEventListener("submit", async (ev) => {
  ev.preventDefault();
  label.textContent = "Sending...";
  statusEl.className = "text-sm text-center hidden";
  try {
    const res = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" },
    });
    if (!res.ok) throw new Error();
    form.reset();
    statusEl.textContent = "Message sent. Thank you!";
    statusEl.className = "text-sm text-center text-green-400";
  } catch {
    statusEl.textContent = "Something went wrong. Please email me directly.";
    statusEl.className = "text-sm text-center text-red-400";
  }
  label.textContent = "Send Message";
});
