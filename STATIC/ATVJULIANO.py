* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #f5f1eb;
    color: #222;
}
header {
    background: #3d2a1f;
    color: white;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}
nav {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}
nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}
.hero {
    background: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)),
                url('https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
    min-height: 420px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: white;
    padding: 20px;
}
.hero-texto {
    max-width: 600px;
}
.hero-texto h2 {
    font-size: 2.5rem;
    margin-bottom: 15px;
}
.hero-texto p {
    font-size: 1.1rem;
    margin-bottom: 20px;
}
.btn {
    display: inline-block;
    background: #d28a2d;
    color: white;
    text-decoration: none;
    padding: 12px 20px;
    border-radius: 8px;
    font-weight: bold;
}
.sobre, .pratos, .contato {
    max-width: 1100px;
    margin: 50px auto;
    padding: 0 20px;
}
.sobre h2, .pratos h2, .contato h2 {
    margin-bottom: 15px;
    color: #3d2a1f;
}
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    margin-top: 20px;
}
.card {
    background: white;
    border: 1px solid #e2d5c7;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.card h3 {
    margin-bottom: 10px;
    color: #3d2a1f;
}
.card span {
    display: inline-block;
    margin-top: 15px;
    color: #b56d1b;
    font-weight: bold;
}
.contato {
    text-align: center;
    margin-bottom: 60px;
}
footer {
    background: #2d211d;
    color: white;
    text-align: center;
    padding: 20px;
}