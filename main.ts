// Apply gravity
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (player2.isHittingTile(CollisionDirection.Bottom)) {
        // Jump force
        player2.vy = -100
    }
})
let player2: Sprite = null
player2 = sprites.create(img`
    . . . . . . . . . . 
    . . . 5 5 5 . . . . 
    . . 5 5 5 5 5 . . . 
    . . 5 5 5 5 5 . . . 
    . . . 5 5 5 . . . . 
    . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(player2, 100, 0)
tiles.setTilemap(tilemap`level`)
scene.cameraFollowSprite(player2)
// Apply gravity
player2.ay = 100
