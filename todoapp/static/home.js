const add_task = document.getElementById('add-task')
const dataContainer = document.getElementById('data')

window.addEventListener("load", () => {
  const sessionKey = window.sessionStorage.getItem('key')

  if(!sessionKey) {
    window.location.href = "http://localhost:8000/"
  }

  const id = getUserId()

  getAllTasksAndRenderData(id)
})

getUserId = () => {
  let session = window.sessionStorage.getItem('key')

  return session.substr(session.indexOf('?')+1, session.length-1)
}

const getAllTasksAndRenderData = (id) => {
  data = []

  axios.get('http://localhost:8000/task/getAll/'+id+'')
    .then(function (response) {
      response.data[1].forEach((i) => {

        data.push(
          "<ul><li>"+i.tsk_id+"</li><li>"+i.tsk_name+"</li><li>"+i.tsk_description+"</li></ul>"
        )
      })

      removeAllChilds(dataContainer)
      
      data.forEach(i => {
        dataContainer.innerHTML += i
      })
    })
    .catch(function (err) {
      console.log(err)
    })
}

removeAllChilds = (el) => {
  let child = el.lastElementChild
  
  while (child) {
    el.removeChild(child)
    child = el.lastElementChild
  }
}

addItemInList = (name, description, id) => {
  try {
    if(axios.post('http://localhost:8000/task/add', {name, description, id})) {
      getAllTasksAndRenderData(id)
    }
  } catch (err) {
    console.log(err)
  }
}

removeItemInList = () => {

}

add_task.addEventListener('click', () => {
  const tsk_name = document.getElementById('name').value
  const tsk_description = document.getElementById('description').value

  addItemInList(tsk_name, tsk_description, getUserId())
})