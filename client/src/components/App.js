import { useState, useEffect } from "react";
import UserPosts from "./Users";
import AddUser from "./AddUser";


function App() {
  const [users, setUsers] = useState([])

  useEffect(()=>{
    fetch('/users')
    .then(r=>r.json())
    .then(data=>setUsers(data))
    // .then(console.log(users))
    .catch((e)=>console.log(e))
  }, [])

  // console.log(users)

  function handleAddUser(user){
    setUsers([...users, user])
  }

  return (
    <div>
      <AddUser handleAddUser={handleAddUser}/>
      <UserPosts users={users}/>
  </div>
  );
}

export default App;
