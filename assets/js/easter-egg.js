(() => {
  const links = [...document.querySelectorAll('.retro-link')];
  const toggle = document.querySelector('#noise-toggle');
  const readout = document.querySelector('.link-readout');
  let audioContext;
  let noiseTimer;
  let noisy = false;

  const context = () => {
    if (!audioContext) {
      audioContext = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioContext.state === 'suspended') audioContext.resume();
    return audioContext;
  };

  const tone = (ctx, {
    frequency = 440,
    endFrequency = frequency,
    duration = .09,
    gain = .045,
    type = 'square',
    delay = 0
  } = {}) => {
    const now = ctx.currentTime + delay;
    const oscillator = ctx.createOscillator();
    const volume = ctx.createGain();
    oscillator.type = type;
    oscillator.frequency.setValueAtTime(frequency, now);
    oscillator.frequency.exponentialRampToValueAtTime(Math.max(30, endFrequency), now + duration);
    volume.gain.setValueAtTime(.0001, now);
    volume.gain.exponentialRampToValueAtTime(gain, now + .008);
    volume.gain.exponentialRampToValueAtTime(.0001, now + duration);
    oscillator.connect(volume).connect(ctx.destination);
    oscillator.start(now);
    oscillator.stop(now + duration + .02);
  };

  const playSound = (kind) => {
    if (!noisy) return;
    const ctx = context();
    if (kind === 'chain') {
      tone(ctx, {frequency: 1280, endFrequency: 720, duration: .045, gain: .024});
      tone(ctx, {frequency: 940, endFrequency: 510, duration: .05, gain: .022, delay: .055});
    } else if (kind === 'folder') {
      tone(ctx, {frequency: 160, endFrequency: 92, duration: .1, gain: .04, type: 'triangle'});
    } else if (kind === 'scanner') {
      tone(ctx, {frequency: 260, endFrequency: 1180, duration: .2, gain: .026, type: 'sawtooth'});
    } else if (kind === 'camera') {
      tone(ctx, {frequency: 1400, endFrequency: 360, duration: .035, gain: .032});
      tone(ctx, {frequency: 780, endFrequency: 760, duration: .06, gain: .018, type: 'sine', delay: .06});
    } else if (kind === 'crt') {
      tone(ctx, {frequency: 90, endFrequency: 820, duration: .22, gain: .028, type: 'sawtooth'});
      tone(ctx, {frequency: 1560, endFrequency: 1550, duration: .1, gain: .012, type: 'sine', delay: .2});
    } else if (kind === 'building') {
      tone(ctx, {frequency: 115, endFrequency: 80, duration: .09, gain: .04, type: 'square'});
      tone(ctx, {frequency: 105, endFrequency: 74, duration: .09, gain: .032, type: 'square', delay: .11});
    } else if (kind === 'plus') {
      tone(ctx, {frequency: 330, endFrequency: 330, duration: .09, gain: .026, type: 'triangle'});
      tone(ctx, {frequency: 495, endFrequency: 495, duration: .11, gain: .026, type: 'triangle', delay: .09});
      tone(ctx, {frequency: 660, endFrequency: 660, duration: .14, gain: .022, type: 'triangle', delay: .18});
    } else if (kind === 'foundation') {
      tone(ctx, {frequency: 125, endFrequency: 76, duration: .07, gain: .045, type: 'square'});
      tone(ctx, {frequency: 110, endFrequency: 64, duration: .08, gain: .038, type: 'square', delay: .09});
    } else if (kind === 'stamp') {
      tone(ctx, {frequency: 150, endFrequency: 42, duration: .065, gain: .052, type: 'square'});
    } else if (kind === 'sign') {
      tone(ctx, {frequency: 920, endFrequency: 910, duration: .38, gain: .035, type: 'sine'});
      tone(ctx, {frequency: 1380, endFrequency: 1360, duration: .3, gain: .02, type: 'sine'});
    } else if (kind === 'branch') {
      tone(ctx, {frequency: 294, endFrequency: 294, duration: .09, gain: .022, type: 'triangle'});
      tone(ctx, {frequency: 392, endFrequency: 392, duration: .1, gain: .022, type: 'triangle', delay: .08});
      tone(ctx, {frequency: 587, endFrequency: 587, duration: .12, gain: .02, type: 'triangle', delay: .16});
    } else if (kind === 'mail') {
      tone(ctx, {frequency: 1180, endFrequency: 940, duration: .22, gain: .028, type: 'sine'});
    } else if (kind === 'typewriter') {
      tone(ctx, {frequency: 820, endFrequency: 210, duration: .025, gain: .028, type: 'square'});
      tone(ctx, {frequency: 650, endFrequency: 170, duration: .025, gain: .022, type: 'square', delay: .045});
    } else if (kind === 'paper') {
      tone(ctx, {frequency: 220, endFrequency: 760, duration: .16, gain: .018, type: 'sawtooth'});
    }
  };

  const setNoise = (enabled) => {
    noisy = enabled;
    toggle.setAttribute('aria-pressed', String(enabled));
    toggle.textContent = enabled ? 'MAKE IT STOP' : 'TURN THE NOISE ON';
    clearInterval(noiseTimer);
    if (enabled) {
      context();
      playSound('sign');
      noiseTimer = setInterval(() => {
        const first = links[Math.floor(Math.random() * links.length)];
        const second = links[Math.floor(Math.random() * links.length)];
        playSound(first.dataset.sound);
        if (second !== first && Math.random() > .45) {
          setTimeout(() => playSound(second.dataset.sound), 120);
        }
      }, 520);
    }
  };

  links.forEach((link) => {
    const announce = () => {
      readout.textContent = link.dataset.label;
      playSound(link.dataset.sound);
    };
    link.addEventListener('pointerenter', announce);
    link.addEventListener('focus', announce);
    link.addEventListener('click', () => playSound(link.dataset.sound));
  });

  toggle.addEventListener('click', () => setNoise(!noisy));
})();
