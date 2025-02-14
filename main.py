# Apply gravity

def on_a_pressed():
    if player2.is_hitting_tile(CollisionDirection.BOTTOM):
        # Jump force
        player2.vy = -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

player2: Sprite = None
player2 = sprites.create(img("""
        . . . . . . . . . . 
            . . . 5 5 5 . . . . 
            . . 5 5 5 5 5 . . . 
            . . 5 5 5 5 5 . . . 
            . . . 5 5 5 . . . . 
            . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(player2, 100, 0)
tiles.set_tilemap(tilemap("""
    level
"""))
scene.camera_follow_sprite(player2)
# Apply gravity
player2.ay = 100