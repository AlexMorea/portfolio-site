// static/js/bg.js
document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("bg-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let w = canvas.width = innerWidth;
  let h = canvas.height = innerHeight;

  // Resize
  window.addEventListener("resize", () => {
    w = canvas.width = innerWidth;
    h = canvas.height = innerHeight;
  });

  // particles
  const N = Math.min(80, Math.floor(w / 12));
  const particles = [];
  for (let i = 0; i < N; i++) {
    particles.push({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: 1 + Math.random() * 3,
      alpha: 0.06 + Math.random() * 0.12
    });
  }

  function draw() {
    ctx.clearRect(0,0,w,h);
    // subtle gradient overlay
    const g = ctx.createLinearGradient(0,0,w,h);
    g.addColorStop(0, "rgba(6,17,36,0.2)");
    g.addColorStop(1, "rgba(6,34,60,0.18)");
    ctx.fillStyle = g;
    ctx.fillRect(0,0,w,h);

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < -50) p.x = w + 50;
      if (p.x > w + 50) p.x = -50;
      if (p.y < -50) p.y = h + 50;
      if (p.y > h + 50) p.y = -50;

      ctx.beginPath();
      ctx.fillStyle = "rgba(14,95,200," + p.alpha + ")";
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    });

    requestAnimationFrame(draw);
  }

  draw();
});
