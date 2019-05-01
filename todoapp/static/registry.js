const submit_signup = document.getElementById('submit-signup')

const registryUser = async (name, cpf, email, password) => {
  try {
    const response = await axios.post('http://localhost:8000/user/add', {
      name, cpf, email, password
    })
    console.log(response)
  } catch (err) {
    console.log(err)
  }
}

submit_signup.addEventListener('click', () => {
  const name = document.getElementById('sigup_nome').value
  const cpf = document.getElementById('sigup_cpf').value
  const email = document.getElementById('sigup_email').value
  const password = document.getElementById('sigup_password').value

  if(registryUser(name, cpf, email, password)) {
    document.getElementById('sigup_nome').value = ''
    document.getElementById('sigup_cpf').value = ''
    document.getElementById('sigup_email').value = ''
    document.getElementById('sigup_password').value = ''
  }
})