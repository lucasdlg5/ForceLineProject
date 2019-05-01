const add_task = document.getElementById('add-task')

window.addEventListener("load", () => {
  const sessionKey = window.sessionStorage.getItem('key')

  if(!sessionKey) {
    window.location.href = "http://localhost:8000/"
  }
})

getUserId = () => {
  
}

getAllTasks = () => {

}

addItemInList = () => {

}

removeItemInList = () => {

}

add_task.addEventListener('click', () => {
  const tsk_name = document.getElementById('name')
  const tsk_description = document.getElementById('description')

  
})