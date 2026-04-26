const resetbtn = document.getElementById("resetButton");

resetbtn.addEventListener("click", () => {
    gameOver = false;
    fetch("/reset", { method: "POST" })
        .then(() => location.reload());
});

let gameOver = false;
const cells = document.querySelectorAll("[data-cell]");
const statusText = document.getElementById("status");
cells.forEach((cell, index) => {
    cell.addEventListener("click", () => {
        if (!gameOver) {
            makeMove(index);
        }
    });
});

function makeMove(square) {
    fetch("/move", {
        method: "POST", 
        headers: {
            "Content-Type": "application/json"
        }, 
        body: JSON.stringify({ square: square })
    })
    .then(response => response.json())
    .then(data => {
        updateBoard(data.board);

        if (data.winner) {
            gameOver = true;
            statusText.innerText = data.winner + " wins!";
            // Highlight winning cells
            if (data.winning_cells && Array.isArray(data.winning_cells)) {
                data.winning_cells.forEach(index => {
                    cells[index].classList.add("won");
                });
            }
            cells.forEach(cell => cell.classList.add("taken"));

        } else if (data.tie) {
            gameOver = true;
            statusText.innerText = "It's a tie!";
            cells.forEach(cell => cell.classList.add("taken"));
        }
    });
}

function updateBoard(board) {
    cells.forEach((cell, index) => {
        cell.innerText = board[index];
        if(board[index] !== " ") {
            cell.classList.add("taken");
        }
    });
}

const multiplayerBtn = document.getElementById("multiPlayer");
const dumbCompBtn = document.getElementById("dumbComp");
const geniusCompBtn = document.getElementById("geniusComp");

multiplayerBtn.addEventListener("click", () => {
    fetch("/set_mode", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mode: "multiplayer" })
    })
    .then(location.reload());

    multiplayerBtn.classList.add("mp");
});

dumbCompBtn.addEventListener("click", () => {
    fetch("/set_mode", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mode: "dumb_computer" })
    })
    .then(location.reload());

    dumbCompBtn.classList.add("dc");
});

geniusCompBtn.addEventListener("click", () => {
    fetch("/set_mode", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mode: "genius_computer" })
    })
    .then(location.reload());

    geniusCompBtn.classList.add("gc");
});

const gridlock = document.getElementById("gridlock");
const gridlock1 = document.getElementById("gridlock1");
gridlock.addEventListener("click", () => {
    window.location.href = "/";
});

gridlock1.addEventListener("click", () => {
    window.location.href = "/";
});


