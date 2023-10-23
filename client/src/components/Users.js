import React from 'react'
import { Card, Icon } from 'semantic-ui-react'

export default function UserPosts({users}) {

  const userList = users.map((user)=>{
    return(
      <>
        <Card key={user.id}>
          <Card.Content header={user.username} />
          {user.posts.map((post)=>(
            <>
              <Card.Content header={post.title} as={'h2'} />
              <Card.Content description={post.body} />
            </>

          ))}
          <Card.Content extra>
            <Icon name='user'/>{user.email}
          </Card.Content>
        </Card>     
      </>

    )

  })

  return (
    <div>{userList}</div>
  )
}
