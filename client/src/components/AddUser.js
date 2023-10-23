import React from 'react'
import { useState } from 'react'
import { Form, Button, Header } from 'semantic-ui-react'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function AddUser({ handleAddUser }) {
    const [username, setUserName] = useState('')
    const [email, setEmail] = useState('')

    function onAddUser(e){
        e.preventDefault();
        const new_user = {
            username: username,
            email: email,
        }

        fetch('/users', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(new_user)
        })
        .then(r => r.json())
        .then(data => handleAddUser(data))
        .catch((e)=> console.log(e))
    }

    function notify(){
        <ToastContainer>
        {toast.success('User Added Successfully!', {
            position: "top-right",
            autoClose: 5000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
            progress: undefined,
            theme: "light",
            })}
        </ToastContainer>
    }

  return (
    <Form onSubmit={onAddUser}>
        <Header as="h3">Add A New User</Header>
        <Form.Group widths="equal" >
            <Form.Input 
                label="Username" 
                placeholder='johndoe'
                onChange={(e)=>setUserName(e.target.value)}
            />
            <Form.Input 
                label="email" 
                placeholder="joe@example.com" 
                onChange={(e)=>setEmail(e.target.value)}
            />
            <Button onClick={()=>notify}>Submit</Button>
        </Form.Group>
    </Form>
  )
}
