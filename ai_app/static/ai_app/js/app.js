function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function callApi(endpoint, target) {
    const prompt = document.getElementById('prompt').value;
    if (!prompt) {
        alert('Please enter a prompt first');
        return;
    }
    
    fetch(`/ai/api/${endpoint}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({prompt: prompt})
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.querySelector(target);
        if (Array.isArray(data.result)) {
            resultElement.innerText = data.result.join(', ');
        } else {
            resultElement.innerText = data.result;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing your request');
    });
}

function playAudio() {
    const prompt = document.getElementById('prompt').value;
    if (!prompt) {
        alert('Please enter text for speech synthesis');
        return;
    }
    
    fetch('/ai/api/tts/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({prompt: prompt})
    })
    .then(response => response.blob())
    .then(blob => {
        const audioUrl = URL.createObjectURL(blob);
        const audio = document.getElementById('ttsAudio');
        audio.src = audioUrl;
        audio.play();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred during speech synthesis');
    });
}

function showPlot() {
    const prompt = document.getElementById('prompt').value;
    if (!prompt) {
        alert('Please enter a prompt for visualization');
        return;
    }
    
    fetch('/ai/api/plot/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({prompt: prompt})
    })
    .then(response => response.blob())
    .then(blob => {
        const plotUrl = URL.createObjectURL(blob);
        const img = document.getElementById('plotImg');
        img.src = plotUrl;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while generating the plot');
    });
}

function processAR() {
    const fileInput = document.getElementById('arInput');
    if (!fileInput.files || !fileInput.files[0]) {
        alert('Please select an image file first');
        return;
    }
    
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);
    
    fetch('/ai/api/ar/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const arUrl = URL.createObjectURL(blob);
        const img = document.getElementById('arImg');
        img.src = arUrl;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while processing the AR image');
    });
}