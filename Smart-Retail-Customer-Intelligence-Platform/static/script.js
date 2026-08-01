// ===========================
// Product Classification
// ===========================

async function predictProduct() {

    const fileInput = document.getElementById("productImage");

    if (fileInput.files.length === 0) {
        alert("Please select a product image.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {

        const response = await fetch("/predict-product", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("productResult").innerHTML =
    "<b>🛍️ Predicted Category:</b> " + data["Predicted Category"];

    } catch (error) {

        console.error(error);

        document.getElementById("productResult").innerHTML =
            "Error while predicting product.";

    }

}


// ===========================
// Sentiment Analysis
// ===========================

async function predictSentiment() {

    const review = document.getElementById("review").value.trim();

    if (review === "") {
        alert("Please enter a review.");
        return;
    }

    try {

        const response = await fetch("/predict-sentiment", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                review: review
            })

        });

        const data = await response.json();
        document.getElementById("sentimentResult").innerHTML =
            "<b>😊 Sentiment:</b> " + data["Sentiment"];

    } catch (error) {

        console.error(error);

        document.getElementById("sentimentResult").innerHTML =
            "Error while analyzing sentiment.";

    }

}


// ===========================
// Face Recognition
// ===========================

async function recognizeFace() {

    const fileInput = document.getElementById("faceImage");

    if (fileInput.files.length === 0) {
        alert("Please select a face image.");
        return;
    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    try {

        const response = await fetch("/recognize-face", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        document.getElementById("faceResult").innerHTML =
        "<b>Recognized Person:</b> " + data["Recognized Person"];
         
    } catch (error) {

        console.error(error);

        document.getElementById("faceResult").innerHTML =
            "Error while recognizing face.";

    }

}


// ===========================
// AI Chatbot
// ===========================

async function chat() {

    const question = document.getElementById("question").value.trim();

    if (question === "") {
        alert("Please enter your question.");
        return;
    }

    document.getElementById("chatResult").innerHTML = "Thinking...";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        if (data.error) {

            document.getElementById("chatResult").innerHTML =
                "<span style='color:red'>" + data.error + "</span>";

        } else {

            document.getElementById("chatResult").innerHTML =
                "<b>🤖 Answer:</b><br>" + data.answer;

        }

    } catch (error) {

        console.error(error);

        document.getElementById("chatResult").innerHTML =
            "Unable to connect to the chatbot.";

    }

}


// ===========================
// Press Enter for Chatbot
// ===========================

document.addEventListener("DOMContentLoaded", function () {

    const questionBox = document.getElementById("question");

    if (questionBox) {

        questionBox.addEventListener("keypress", function (event) {

            if (event.key === "Enter") {

                event.preventDefault();

                chat();

            }

        });

    }

});