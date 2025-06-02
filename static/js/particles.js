/* particles.js */
document.addEventListener('DOMContentLoaded', () => {
  tsParticles.load('tsparticles', {
    fpsLimit: 60,
    background: {
      color: { value: "#111" }  /* coincide con el fondo del body */
    },
    particles: {
      number: { value: 60, density: { enable: true, area: 800 } },
      color: { value: "#ffffff" },
      shape: { type: "circle" },
      opacity: { value: 0.2, random: false, anim: { enable: false } },
      size: { value: 2, random: { enable: true, minimumValue: 1 } },
      links: {
        enable: true,
        distance: 120,
        color: "#ffffff",
        opacity: 0.15,
        width: 1
      },
      move: {
        enable: true,
        speed: 1.5,
        direction: "none",
        random: false,
        straight: false,
        outMode: "out",
        bounce: false
      }
    },
    interactivity: {
      detectsOn: "canvas",
      events: {
        onHover: { enable: false, mode: "grab" },
        onClick: { enable: false },
        resize: true
      },
      modes: {
        grab: { distance: 140, links: { opacity: 0.25 } }
      }
    },
    retinaDetect: true
  });
});
