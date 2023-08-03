function insert() {
  const insertNickname = document.getElementById('insert-nickname').value;
  const insertEmail = document.getElementById('insert-email').value;
  const insertPassword = document.getElementById('insert-password').value;

  fetch('/insert', {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({ nickname: insertNickname, email: insertEmail, password: insertPassword}),
  })
  .then((response) => response.json())
  .then(data => {
    let resultWrap = document.querySelector('.insert-select-result-wrap');
    resultWrap.innerHTML = '';

    let h3 = document.createElement('h3');
    h3.setAttribute('class', 'insert-result');
    h3.textContent = data.msg;
    resultWrap.appendChild(h3);
  })
  .catch(Error => {
    console.log(Error);
  });
}

function select() {
  const selectNickname = document.getElementById('select-nickname').value;
  const selectPassword = document.getElementById('select-password').value;

  fetch('/select', {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({nickname: selectNickname, password: selectPassword}),
  })
  .then((response) => response.json())
  .then(data => {
    result = data.data
    let selectDiv = document.querySelector('.insert-select-result-wrap');
    selectDiv.innerHTML = '';

    result.forEach(data => {
      let resultWrap = document.createElement('div');
      resultWrap.setAttribute('class', 'insert-select-result-wrap')
      
      let p_id = document.createElement('p');
      p_id.setAttribute('class', 'select-result-id');
      p_id.textContent = 'id = ' + data.id;
      resultWrap.appendChild(p_id);
      
      let p_email = document.createElement('p');
      p_email.setAttribute('class', 'select-result-email');
      p_email.textContent = 'email = ' + data.email;
      resultWrap.appendChild(p_email);

      let p_nickname = document.createElement('p');
      p_nickname.setAttribute('class', 'select-result-nickname');
      p_nickname.textContent = 'nickname = ' + data.nickname;
      resultWrap.appendChild(p_nickname);

      let p_password = document.createElement('p');
      p_password.setAttribute('class', 'select-result-password');
      p_password.textContent = 'password = ' + data.password;
      resultWrap.appendChild(p_password);

      selectDiv.appendChild(resultWrap)
    })
  })
  .catch(Error => {
    console.log(Error);
  });
}