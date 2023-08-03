function urlShort() {
  const api_key = "6M3l4FsOM2kQQRk8eRbZmbzG0ySLLIRM";
  const url = "https://api.lrl.kr/v5/url/short";
  const inputUrl = document.getElementById('short-input').value;

  fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({ "key": api_key, "url": inputUrl }),
  })
  .then(response => {
    if (!response.ok) {
      return response.json().then(errorData => {
        throw { status: response.status, error: errorData };
      });
    }
    return response.json();
  })
  .then(data => {
    console.log(data)
  })
  .catch(Error => {
    console.log(Error);
  });
}

(function () {
  confirm("test")
})();