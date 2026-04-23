window.onload = () => {
  const buttons = document.querySelectorAll('button');
  const labels = ["Secret", "Admin", "Debug", "Flag", "Free Flag", "Click to see flag"];
  const btnIds = ["btn1", "btn2", "btn3", "btn4"];

  // Menja ID dugmadi svakih 0.9s
  setInterval(() => {
    buttons.forEach(button => {
      if (Math.random() < 0.1) { // 10% šanse
        let currentId = button.id;
        let newId;
        // Izaberi nasumični ID koji NIJE trenutni
        do {
          newId = btnIds[Math.floor(Math.random() * btnIds.length)];
        } while(newId === currentId);
        button.id = newId;
      }
    });
  }, 900);

  // Menja label dugmadi svakih 0.9s
  setInterval(() => {
    buttons.forEach(button => {
      if (Math.random() < 0.1) {
        button.innerText = labels[Math.floor(Math.random() * labels.length)];
      }
    });
  }, 900);

  // Shuffle dugmadi vizuelno (flex container potreban)
  const container = document.getElementById('divall');
  function shuffleVisual() {
    const order = [...buttons].sort(() => Math.random() - 0.5);
    order.forEach((btn, index) => {
      btn.style.order = index; 
    });
  }
  setInterval(shuffleVisual, 3000);
};