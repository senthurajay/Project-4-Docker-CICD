
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Snake Game - CI/CD Project</title>
        <style>
            body {
                background: #151515;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            h1 {
                color: #00ff88;
            }

            canvas {
                background: black;
                border: 3px solid #00ff88;
            }

            button {
                padding: 12px 25px;
                margin: 15px;
                background: #00ff88;
                border: none;
                cursor: pointer;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <h1>🐍 Snake Game</h1>
        <h3>Docker CI/CD Project</h3>

        <h2>Score: <span id="score">0</span></h2>

        <canvas id="game" width="400" height="400"></canvas>

        <br>
        <button onclick="startGame()">Start Game</button>

        <p>Use Arrow Keys to move the snake.</p>

        <script>
            const canvas = document.getElementById("game");
            const ctx = canvas.getContext("2d");

            let snake = [{x: 200, y: 200}];
            let food = {x: 100, y: 100};
            let dx = 20;
            let dy = 0;
            let score = 0;
            let running = false;
            let timer;

            function draw() {
                ctx.fillStyle = "black";
                ctx.fillRect(0, 0, 400, 400);

                ctx.fillStyle = "red";
                ctx.fillRect(food.x, food.y, 20, 20);

                ctx.fillStyle = "#00ff88";
                snake.forEach(part => {
                    ctx.fillRect(part.x, part.y, 18, 18);
                });
            }

            function move() {
                let head = {
                    x: snake[0].x + dx,
                    y: snake[0].y + dy
                };

                if (
                    head.x < 0 || head.x >= 400 ||
                    head.y < 0 || head.y >= 400 ||
                    snake.some(part => part.x === head.x && part.y === head.y)
                ) {
                    clearInterval(timer);
                    running = false;
                    alert("Game Over! Your score: " + score);
                    return;
                }

                snake.unshift(head);

                if (head.x === food.x && head.y === food.y) {
                    score += 10;
                    document.getElementById("score").innerText = score;

                    food = {
                        x: Math.floor(Math.random() * 20) * 20,
                        y: Math.floor(Math.random() * 20) * 20
                    };
                } else {
                    snake.pop();
                }

                draw();
            }

            document.addEventListener("keydown", function(e) {
                if (e.key === "ArrowUp" && dy === 0) {
                    dx = 0; dy = -20;
                }
                if (e.key === "ArrowDown" && dy === 0) {
                    dx = 0; dy = 20;
                }
                if (e.key === "ArrowLeft" && dx === 0) {
                    dx = -20; dy = 0;
                }
                if (e.key === "ArrowRight" && dx === 0) {
                    dx = 20; dy = 0;
                }
            });

            function startGame() {
                clearInterval(timer);
                snake = [{x: 200, y: 200}];
                food = {x: 100, y: 100};
                dx = 20;
                dy = 0;
                score = 0;
                document.getElementById("score").innerText = score;
                running = true;
                draw();
                timer = setInterval(move, 150);
            }

            draw();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
