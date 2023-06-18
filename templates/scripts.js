
document.addEventListener('DOMContentLoaded', function() {
  var recordButton = document.getElementById('recordButton');
  var resultDiv = document.getElementById('result');
  var correctionForm = document.getElementById('correctionForm');
  var correctionText = document.getElementById('correctionText');
  var submitButton = document.getElementById('submitButton');

  recordButton.addEventListener('click', function() {
    recordButton.disabled = true;
    resultDiv.innerHTML = 'Aufnahme läuft für 10s...';
    correctionText.value = '';
    // Code für die Aufnahme und die Spracherkennung
    fetch('/transcribe', { method: 'POST' })
      .then(response => response.json())
      .then(data => {
        resultDiv.innerHTML = 'Textausgabe: ' + data.text;
        correctionForm.style.display = 'block';
        correctionText.value = data.text; // Den erkannten Text im Korrekturtextfeld anzeigen
        recordButton.disabled = false; // Aufnahmeschaltfläche wieder aktivieren
        
      })
      .catch(error => {
        console.error('Fehler:', error);
        recordButton.disabled = false; // Aufnahmeschaltfläche wieder aktivieren
      });
  });

  correctionForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var correction = correctionText.value;

    // Anzeige des korrigierten Texts im selben Feld
    resultDiv.innerHTML = 'Textausgabe: <span class="text-to-correct">' + correction + '</span>';

    // Senden des korrigierten Texts an den Server
    fetch('/correct', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ correction: correction })
    })
      .then(response => response.json())
      .then(data => {
        // Anzeigen der Antwort des Servers
        resultDiv.innerHTML += '<br><br>Antwort: ' + data.response;
      })
      .catch(error => {
        console.error('Fehler:', error);
      });
  });
});
