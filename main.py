<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Spanish City RP — Valencia | ERLC</title>
  <meta name="description" content="Servidor ERLC Spanish City RP — roleplay inspirado en Valencia. Únete a nuestra comunidad en Discord para eventos, roles y normativa.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" crossorigin="anonymous">
  <style>
    :root{
      --accent:#e04b3a; /* naranja/rojo Valenciano */
      --dark:#0f1724;
      --muted:#6b7280;
      --glass: rgba(255,255,255,0.06);
      font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }
    *{box-sizing:border-box}
    body{margin:0;background:linear-gradient(180deg,#071019 0%, #0b1320 100%);color:#e6eef8;min-height:100vh}
    header{backdrop-filter:blur(6px);position:sticky;top:0;z-index:40;background:linear-gradient(180deg, rgba(10,14,20,0.6), rgba(10,14,20,0.35));border-bottom:1px solid rgba(255,255,255,0.03)}
    .container{max-width:1100px;margin:0 auto;padding:1rem}
    .nav{display:flex;gap:1rem;align-items:center;justify-content:space-between}
    .brand{display:flex;gap:.75rem;align-items:center}
    .brand .logo{width:46px;height:46px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#ffb86b);display:flex;align-items:center;justify-content:center;font-weight:800;color:#071018}
    nav ul{display:flex;gap:0.5rem;list-style:none;margin:0;padding:0}
    nav a{color:inherit;text-decoration:none;padding:.6rem .8rem;border-radius:8px;font-weight:600}
    nav a:hover{background:rgba(255,255,255,0.02)}
    .cta{background:var(--accent);color:#071018;padding:.6rem .9rem;border-radius:10px;font-weight:700}

    /* Botón fijo de Discord (esquina superior derecha) */
    #fixedDiscord{position:fixed;top:12px;right:12px;background:#5865f2;color:white;padding:.6rem .9rem;border-radius:10px;font-weight:700;z-index:9999;box-shadow:0 6px 20px rgba(88,101,242,0.18);text-decoration:none;display:inline-flex;gap:.5rem;align-items:center}
    #fixedDiscord i{font-size:1rem}
    @media (max-width:420px){#fixedDiscord{right:8px;top:8px;padding:.45rem .6rem;font-size:.95rem}}

    /* Hero */
    .hero{display:grid;grid-template-columns:1fr 420px;gap:2rem;align-items:center;padding:3rem 0}
    .hero .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:2rem;border-radius:14px;border:1px solid rgba(255,255,255,0.03)}
    h1{margin:0;font-size:2.2rem}
    p.lead{color:var(--muted);margin-top:.6rem}
    .hero-grid{display:flex;gap:1rem;margin-top:1.3rem}
    .pill{background:var(--glass);padding:.45rem .7rem;border-radius:999px;font-weight:700}
    .server-info{display:flex;flex-direction:column;gap:.6rem}
    .big-ip{font-size:1.2rem;font-weight:800}
    .discord-btn{display:inline-flex;gap:.6rem;align-items:center;padding:.6rem .9rem;background:#5865f2;color:white;border-radius:10px;text-decoration:none}

    /* Sections */
    section{padding:2.2rem 0}
    .grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
    .card-plain{background:rgba(255,255,255,0.02);padding:1rem;border-radius:10px;border:1px solid rgba(255,255,255,0.03)}

    /* Rules / Staff list */
    .rules li{margin-bottom:.6rem}
    .staff{display:flex;gap:.8rem;align-items:center}
    .avatar{width:54px;height:54px;border-radius:10px;background:linear-gradient(180deg,#fff2,#0000);display:flex;align-items:center;justify-content:center;font-weight:700;color:#071018}

    /* Events */
    .events .event{display:flex;justify-content:space-between;padding:.8rem;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.02));border-radius:8px}

    /* Footer */
    footer{padding:2rem 0;border-top:1px solid rgba(255,255,255,0.03);color:var(--muted)}

    /* Responsive */
    @media (max-width:900px){
      .hero{grid-template-columns:1fr;}
      .grid-3{grid-template-columns:1fr}
      nav ul{display:none}
      .mobile-menu{display:inline-flex}
    }
  </style>
</head>
<body>
  <a id="fixedDiscord" href="https://discord.gg/UTQS4Q9Wpn" target="_blank" rel="noopener" aria-label="Unirse al Discord"><i class="fa-brands fa-discord"></i>&nbsp;Unirse al Discord</a>
  <header>
    <div class="container nav">
      <div class="brand">
        <div class="logo">SC</div>
        <div>
          <div style="font-weight:800">Spanish City RP</div>
          <div style="font-size:.8rem;color:var(--muted)">Roleplay inspirado en Valencia • ERLC</div>
        </div>
      </div>
      <nav>
        <ul>
          <li><a href="#about">Sobre</a></li>
          <li><a href="#rules">Normas</a></li>
          <li><a href="#staff">Staff</a></li>
          <li><a href="#events">Eventos</a></li>
          <li><a href="#join">Unirse</a></li>
        </ul>
      </nav>
      <div style="display:flex;gap:.6rem;align-items:center">
        <a class="cta" href="#join">Unirse</a>
        <button class="mobile-menu" style="display:none;background:transparent;border:0;color:inherit"><i class="fa fa-bars"></i></button>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <div class="card">
        <h1>Spanish City RP — Valencia</h1>
        <p class="lead">Servidor ERLC centrado en roleplay urbano y servicios públicos. Vive historias como policía local, bombero, sanitario o civil en una ciudad inspirada por Valencia: playas, fallas, y tráfico realista.</p>
        <div class="hero-grid">
          <div class="pill">Modos: ERLC / Realista</div>
          <div class="pill">Slots: 128</div>
          <div class="pill">Facciones: Policía, Bomberos, Emergencias, Civiles</div>
        </div>

        <div style="margin-top:1.4rem" class="server-info">
          <div style="display:flex;gap:.6rem;align-items:center">
            <div class="big-ip">IP: <span style="font-weight:900">play.spanishcityrp.es</span></div>
            <div style="color:var(--muted);font-size:.95rem">Puerto: 30120</div>
          </div>

          <div style="display:flex;gap:.6rem;margin-top:.8rem">
            <a class="discord-btn" href="https://discord.gg/UTQS4Q9Wpn" id="discordInvite"><i class="fa-brands fa-discord"></i> Unirse al Discord</a>
            <a class="cta" href="#rules" style="background:transparent;border:1px solid rgba(255,255,255,0.03);color:inherit">Leer reglas</a>
          </div>
        </div>

        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.03);margin:1.2rem 0">
        <div style="display:flex;gap:1rem;align-items:center">
          <div style="flex:1">
            <h3 style="margin:0">¿Qué ofrecemos?</h3>
            <p style="margin:.4rem 0;color:var(--muted)">Economía realista, formación para cuerpos, actividades semanales (carreras, simulacros, eventos temáticos) y soporte activo del staff.</p>
          </div>
          <div style="width:160px;text-align:center">
            <!-- Placeholder for a Valencia photo -->
            <img src="https://images.unsplash.com/photo-1541446654331-8f63ff1f6d3b?q=80&w=600&auto=format&fit=crop&ixlib=rb-4.0.3&s=placeholder" alt="Valencia skyline" style="width:100%;border-radius:8px;">
            <div style="font-size:.8rem;color:var(--muted);margin-top:.4rem">Imagen representativa — reemplázala</div>
          </div>
        </div>
      </div>

      <aside style="position:relative">
        <div class="card-plain">
          <h3 style="margin-top:0">Próximos eventos</h3>
          <div class="events">
            <div class="event"><div><strong>Simulacro Bomberos</strong><div style="font-size:.85rem;color:var(--muted)">Sábado • 20:00</div></div><div>Inscritos: 12</div></div>
            <div class="event" style="margin-top:.6rem"><div><strong>Desfile Fallas RP</strong><div style="font-size:.85rem;color:var(--muted)">Domingo • 18:00</div></div><div>Plazas abiertas</div></div>
            <div class="event" style="margin-top:.6rem"><div><strong>Prácticas Policía</strong><div style="font-size:.85rem;color:var(--muted)">Viernes • 21:30</div></div><div>Comando activo</div></div>
          </div>
          <a href="#events" style="display:inline-block;margin-top:1rem;text-decoration:none;padding:.5rem .7rem;border-radius:8px;border:1px solid rgba(255,255,255,0.03)">Ver calendario</a>
        </div>

        <div style="height:16px"></div>

        <div class="card-plain">
          <h4 style="margin-top:0">Unidades principales</h4>
          <div style="display:flex;flex-direction:column;gap:.6rem">
            <div class="pill">Policía Local</div>
            <div class="pill">SAMU / Ambulancias</div>
            <div class="pill">Bomberos</div>
          </div>
        </div>
      </aside>
    </section>

    <section id="about">
      <div class="card-plain">
        <h2>Sobre Spanish City RP</h2>
        <p style="color:var(--muted)">Spanish City RP es un servidor ERLC inspirado en la cultura, arquitectura y vida urbana de Valencia. Nuestro objetivo es crear historias memorables con una comunidad respetuosa y reglas claras.</p>
      </div>
    </section>

    <section id="rules">
      <h2>Normas principales</h2>
      <div class="grid-3" style="margin-top:1rem">
        <div class="card-plain">
          <h3>Respeto</h3>
          <ul class="rules">
            <li>No insultos ni discriminación.</li>
            <li>Roleplay sobre roleplay: evita romper la inmersión.</li>
          </ul>
        </div>
        <div class="card-plain">
          <h3>RP y OOC</h3>
          <ul class="rules">
            <li>Usa OOC solo donde esté permitido.</li>
            <li>Prohibido metajuego y powergame.</li>
          </ul>
        </div>
        <div class="card-plain">
          <h3>Sanciones</h3>
          <ul class="rules">
            <li>Las sanciones se aplican según la gravedad: aviso, kick, ban temporal y ban permanente.</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="staff">
      <h2>Equipo</h2>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:1rem">
        <div class="card-plain staff">
          <div class="avatar">M</div>
          <div>
            <div style="font-weight:800">MarcOficial</div>
            <div style="color:var(--muted);font-size:.9rem">Fundador • Administrador</div>
          </div>
        </div>
        <div class="card-plain staff">
          <div class="avatar">A</div>
          <div>
            <div style="font-weight:800">Alicia</div>
            <div style="color:var(--muted);font-size:.9rem">Jefa Policía</div>
          </div>
        </div>
        <div class="card-plain staff">
          <div class="avatar">S</div>
          <div>
            <div style="font-weight:800">Sergio</div>
            <div style="color:var(--muted);font-size:.9rem">Coordinador Eventos</div>
          </div>
        </div>
      </div>
    </section>

    <section id="events">
      <h2>Calendario</h2>
      <div class="card-plain" style="margin-top:1rem">
        <p style="color:var(--muted)">Aquí puedes integrar un calendario público (Google Calendar o similar) o una tabla con eventos. Ejemplo rápido:</p>
        <table style="width:100%;border-collapse:collapse;margin-top:1rem">
          <thead style="text-align:left;color:var(--muted)"><tr><th>Fecha</th><th>Evento</th><th>Hora</th></tr></thead>
          <tbody>
            <tr><td>05/10/2025</td><td>Prácticas Policía</td><td>21:30</td></tr>
            <tr><td>12/10/2025</td><td>Simulacro Bomberos</td><td>20:00</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section id="join">
      <h2>Cómo unirse</h2>
      <div class="grid-3" style="margin-top:1rem">
        <div class="card-plain">
          <h3>1. Conéctate al servidor</h3>
          <p style="color:var(--muted)">IP: <strong>play.spanishcityrp.es:30120</strong></p>
        </div>
        <div class="card-plain">
          <h3>2. Únete al Discord</h3>
          <p style="color:var(--muted)">Haz clic en el botón superior derecho o en cualquiera de los enlaces de "Unirse al Discord" para acceder a nuestra comunidad.</p>
        </div>
        <div class="card-plain">
          <h3>3. Reglas iniciales</h3>
          <p style="color:var(--muted)">Lee las normas al entrar y pasa por <strong>#bienvenida</strong> para asignarte roles y acceder a canales.</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="container">
    <div style="display:flex;justify-content:space-between;align-items:center">
      <div>© Spanish City RP — Inspirado en Valencia</div>
      <div style="color:var(--muted)">¿Necesitas ayuda? <a href="https://discord.gg/UTQS4Q9Wpn" style="color:inherit;text-decoration:underline">Únete al Discord</a></div>
    </div>
  </footer>
</body>
</html>
