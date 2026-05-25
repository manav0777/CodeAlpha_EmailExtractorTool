const fileInput = document.getElementById("file-input");

const fileName = document.getElementById("file-name");

const form = document.getElementById("upload-form");

const extractButton = document.getElementById("extract-btn");

const uploadBox = document.querySelector(".upload-box");

const copyBtn = document.getElementById("copy-btn");

const clearBtn = document.getElementById("clear-btn");





// File Selection

fileInput.addEventListener("change", () => {

    if (!fileInput.files.length) return;

    const selectedFile = fileInput.files[0].name;

    fileName.innerHTML = `✅ ${selectedFile}`;

    uploadBox.innerHTML = `

        📄 <span style="color:white;">${selectedFile}</span>

    `;
});





// Loading State

form.addEventListener("submit", (event) => {

    if (!fileInput.files.length) {

        alert("Please select a file first!");

        event.preventDefault();

        return;
    }

    extractButton.innerHTML = "⏳ Extracting...";

    extractButton.disabled = true;

    extractButton.style.opacity = "0.7";
});





// Copy Emails

if (copyBtn) {

    copyBtn.addEventListener("click", () => {

        const emails = document.querySelectorAll(".email-list p");

        const text = [...emails]

            .map(email => email.innerText)

            .join("\n");

        navigator.clipboard.writeText(text);

        copyBtn.innerText = "Copied!";

        setTimeout(() => {

            copyBtn.innerText = "Copy";

        }, 2000);
    });
}





// Clear Output

if (clearBtn) {

    clearBtn.addEventListener("click", () => {

        window.location.href = "/";

    });
}