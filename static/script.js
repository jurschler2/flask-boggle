const $guessForm = $('#guess-form');
const $wordInput = $('#word-input');
const $wordMsg = $('#word-msg');
const $scoreBoard = $('#scoreboard');
let wordScore = 0;

$(async function() {

  $guessForm.on('submit', async function(evt) {
    evt.preventDefault();

    let word = $wordInput.val();

    let response = await checkWord(word);

    appendMessage(response);

  });

});


async function checkWord(wordInput) {
  
  let response = await axios.get("/check-word", {params: {
    wordInput
  }});

  return response;
}

function appendMessage(wordMessage) {

  console.log(wordMessage);
  let message = wordMessage.data.result;

  if (message === "ok") {

    let word = wordMessage.config.params.wordInput;
    wordScore += word.length;

    $scoreBoard.text(wordScore);

  }

  $wordMsg.append(`<p>${message}</p>`);
}