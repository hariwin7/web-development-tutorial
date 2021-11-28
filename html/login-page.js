function signIn() {
  const username = document.getElementById("username-field").value;
  const password = document.getElementById("password-field").value;
  const loginErrorMsg = document.getElementById("login-error-msg");

  //   console.log(username, password);

  if (username === "user" && password === "web_dev") {
    alert("You have successfully logged in.");
  } else {
    loginErrorMsg.style.opacity = 1;
  }

  //   fetch("http://127.0.0.1:5000/", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({ username, password }),
  //   })
  //     .then((response) => response.json())
  //     .then((json) => {
  //       if (json.status) alert("You have successfully logged in.");
  //       else loginErrorMsg.style.opacity = 1;
  //     });
}
