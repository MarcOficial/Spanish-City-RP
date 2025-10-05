from flask import Flask, render_template_string

app = Flask(__name__)

# Contenido HTML principal (pegado directamente aquí)
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Spanish City RP | ERLC</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
    body {
      font-family: 'Poppins', sans-serif;
      margin: 0;
      padding: 0;
      background: #0a0a0a;
      color: white;
    }
    header {
      background: linear-gradient(90deg, #ff6600, #ff9900);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    header h1 {
      font-size: 1.6rem;
      font-weight: 700;
    }
    #fixedDiscord {
      position: fixed;
      top: 12px;
      right: 12px;
      background: #5865f2;
      color: white;
      padding: 0.6rem 0.9rem;
      border-radius: 10px;
      font-weight: 700;
      z-index: 9999;
      box-shadow: 0 6px 20px rgba(88, 101, 242, 0.18);
      text-decoration: none;
      display: inline-flex;
      gap: 0.5rem;
      align-items: center;
    }
    main {
      padding: 2rem;
      text-align: center;
    }
    section {
      background: #1a1a1a;
      border-radius: 12px;
      padding: 2rem;
      margin: 2rem auto;
      max-width: 800px;
      box-shadow: 0 0 10px rgba(255,255,255,0.1);
    }
    h2 {
      color: #ff9900;
      border-bottom: 2px solid #ff9900;
      display: inline-block;
      padding-bottom: 0.5rem;
      margin-bottom: 1rem;
    }
    .role {
      color: #ffcc00;
      margin-top: 1.2rem;
      font-weight: bold;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    li {
      margin: 0.3rem 0;
    }
  </style>
</head>
<body>
  <a id="fixedDiscord" href="https://discord.gg/UTQS4Q9Wpn" target="_blank" rel="noopener" aria-label="Unirse al Discord"><i class="fa-brands fa-discord"></i> Unirse al Discord</a>
  <header>
    <h1>Spanish City RP | Inspirado en Valencia</h1>
  </header>
  <main>
    <section>
      <h2>Miembros del Staff</h2>
      <div class="role">〘⚜️〙Creador (CRD)</div>
      <ul><li>@〘⚜〙Marc</li></ul>

      <div class="role">〘🌴〙Co Creador (CCRD)</div>
      <ul><li>@〘🌴〙Mateo</li></ul>

      <div class="role">〘👑〙Propietario/a (PROP)</div>
      <ul><li>@〘👑〙Lin.</li></ul>

      <div class="role">〘✨〙Co Propietario/a (COPROP)</div>
      <ul>
        <li>@〘✨〙Harry</li>
        <li>@〘✨〙kalajan232</li>
      </ul>

      <div class="role">ALTA DIRECTIVA</div>

      <div class="role">〘🎬〙Director Administración (DA)</div>
      <ul>
        <li>@〘🎬〙Mando</li>
        <li>@〘🎬〙Paneterancio</li>
      </ul>

      <div class="role">〘🔍〙Coordinador Staff (CS)</div>
      <ul><li>N/A</li></ul>

      <div class="role">DIRECCIÓN MEDIA</div>

      <div class="role">〘🟢〙Supervisor Jefe (SJ)</div>
      <ul><li>@〘🟢〙Maquinarex1</li></ul>

      <div class="role">〘🔵〙Supervisor (SJ)</div>
      <ul><li>@〘🔵〙Urban</li></ul>

      <div class="role">SUPERVISIÓN Y GESTIÓN</div>

      <div class="role">〘🟣〙Administrador (ADM)</div>
      <ul>
        <li>@〘🟣〙Domínguez</li>
        <li>@〘🟣〙Kaytipo</li>
      </ul>

      <div class="role">〘🔴〙Moderador (MOD)</div>
      <ul>
        <li>@〘🔴〙Antonio</li>
        <li>@〘🔴〙Joel</li>
      </ul>

      <div class="role">〘🟤〙Moderador Aprendiz (MA)</div>
      <ul>
        <li>@〘🟤〙Lostigres</li>
        <li>@〘🟤〙Rafael</li>
      </ul>

      <div class="role">EQUIPO MODERATIVO Y ADMINISTRATIVO</div>

      <div class="role">〘🟡〙Soporte (SOP)</div>
      <ul><li>N/A</li></ul>

      <div class="role">〘🟠〙Soporte Aprendiz (SA)</div>
      <ul><li>@〘🟠〙Aitor</li></ul>
    </section>
  </main>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
