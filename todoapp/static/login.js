const submit_signin = document.getElementById('submit-signin')

const makeLogin = async (email, password) => {
  try {
    const response = await axios.post('http://localhost:8000/user/login', {email, password})
    console.log(response.data)
    if (response.data.email.length > 0) {
      window.location.href = "http://localhost:8000/home"
      window.sessionStorage.setItem("key", response.data.email+"?"+response.data.id)
    }
  } catch (err) {
    console.log(err)
  }
}

submit_signin.addEventListener('click', () => {
  const email = document.getElementById('signin_email').value
  const password = document.getElementById('signin_pass').value
  makeLogin(email, password)
})