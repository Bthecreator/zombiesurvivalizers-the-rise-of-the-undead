def on_a_pressed():
    global bullet
    if direction == 1:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 5 5 5 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player1,
            300,
            0)
    if direction == 0:
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 5 5 5 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player1,
            -300,
            0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    pause(500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.disintegrate, 500)
    info.change_score_by(10)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

bullet: Sprite = None
direction = 0
Player1: Sprite = None
scene.set_background_image(img("""
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeefbbbbbbbfeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeefffffffeeeeeeee
        eefbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeee
        efbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeee
        efbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeee
        efbbfffffffbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeee
        efbfbbffbbbbbfeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeefbbfffffffbbfeeeee
        efbbbbbbbbbbbfeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeefbfbbffbbbbbfeeeee
        efbffbffbbffbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeee
        efbfbffffffbbfeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeefbffbffbbffbfeeeee
        efbbbbbbbbbbbfeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeefbfbffffffbbfeeeee
        efbbbffffffbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeee
        efbbffbbbbffbfeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeefbbbffffffbbfeeeee
        efbbfbbbbbbbbfeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeefbbffbbbbffbfeeeee
        efbbbffbbfffffeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeefbbfbbbbbbbbfeeeee
        effffeffffeeefeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeefbbbffbbfffffeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeffffeffffeeefeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeefffffffeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeefbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeee
        eeeefbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbfffffffbbfeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeefbbfffffffbbfeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeefbfbbffbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbffbffbbffbfeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeee
        eeefbffbffbbffbfeeeeeeeeeeeeefbfbffffffbbfeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeefbfbffffffbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbffffffbbfeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeee
        eeefbbbffffffbbfeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeefbbffbbbbffbfeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeee
        eeefbbfbbbbbbbbfeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeee
        eeefbbbffbbfffffeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeee
        eeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeefffffffeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbfeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeee
        eeeeeefffffffeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeefbbfffffffbbfeee
        eeeeefbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbfbbffbbbbbfeee
        eeeefbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeefbffbffbbffbfeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbfbffffffbbfeee
        eeefbbfffffffbbfeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeee
        eeefbfbbffbbbbbfeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeefbbbffffffbbfeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeefbbffbbbbffbfeee
        eeefbffbffbbffbfeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeefbbfbbbbbbbbfeee
        eeefbfbffffffbbfeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeefbbbffbbfffffeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeee
        eeefbbbffffffbbfeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeefbbffbbbbffbfeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeefbbfbbbbbbbbfeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeefbbbffbbfffffeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeffffeffffeeefeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeeeeeefffffffeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeeeeefbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeee
        eeeeefbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeee
        eeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeefbffbffbbffbfeeeeeeeeee
        eeeefbbfffffffbbfeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeefbfbffffffbbfeeeeeeeeee
        eeeefbfbbffbbbbbfeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeee
        eeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbffffffbbfeeeeeeeeee
        eeeefbffbffbbffbfeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeee
        eeeefbfbffffffbbfeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeee
        eeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeefbbbffbbfffffeeeeeeeeee
        eeeefbbbffffffbbfeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeffffeffffeeefeeeeeeeeee
        eeeefbbffbbbbffbfeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeefbbfbbbbbbbbfeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeefbbbffbbfffffeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeffffeffffeeefeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeee
        eeeeeefffffffeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeeeeefffffffeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeee
        eeeeefbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeeeeefbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeee
        eeeefbbbbbbbbbfeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeeefbbbbbbbbbfeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeeeeeeefbbfffffffbbfeeeeee
        eeefbbfffffffbbfeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeeeefbbfffffffbbfeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeee
        eeefbfbbffbbbbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeefbfbbffbbbbbfeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeeeeeeefbffbffbbffbfeeeeee
        eeefbffbffbbffbfeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeeeefbffbffbbffbfeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeeeeeeefbfbffffffbbfeeeeee
        eeefbfbffffffbbfeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeeeefbfbffffffbbfeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeee
        eeefbbbbbbbbbbbfeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeeeefbbbbbbbbbbbfeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeeeeeeefbbbffffffbbfeeeeee
        eeefbbbffffffbbfeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeeeefbbbffffffbbfeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeee
        eeefbbffbbbbffbfeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeeeefbbffbbbbffbfeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeee
        eeefbbfbbbbbbbbfeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeeeefbbfbbbbbbbbfeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeeeeeefbbbffbbfffffeeeeee
        eeefbbbffbbfffffeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeefbbbffbbfffffeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeffffeffffeeefeeeeee
        eeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffeffffeeefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
info.set_life(5)
Player1 = sprites.create(img("""
        . . . . f f f f f . . . . . . . 
            . . . f 1 1 1 1 1 f . . . . . . 
            . . . f 1 1 1 8 1 f . . . . . . 
            . . . f 1 1 1 8 1 f . . . . . . 
            . . . f 1 1 1 1 1 f . . . . . . 
            . . . f 1 1 1 8 8 f . . . . . . 
            . . . . f f f f f . . . . b . . 
            . . . . . . f . . b b b b b . . 
            . . . . . . f . f b b b . . . . 
            . . . . . . f f . b . . . . . . 
            . . . . . . f . . b . . . . . . 
            . . . . . . f . . . . . . . . . 
            . . . . . . f . . . . . . . . . 
            . . . . . f . f . . . . . . . . 
            . . . . f . . . f . . . . . . . 
            . . . f . . . . . f . . . . . .
    """),
    SpriteKind.player)
zombie = sprites.create(img("""
        . . . . . . . 7 7 7 7 7 . . . . 
            . . . . . . 7 7 7 7 7 7 7 . . . 
            . . . . . . 7 7 2 7 7 7 7 . . . 
            . . . . . . 7 7 2 7 7 7 7 . . . 
            . . . . . . 7 7 7 7 7 7 7 . . . 
            . . . . . . 7 2 2 7 7 7 7 . . . 
            . . . . . . . 7 7 7 7 7 . . . . 
            . . . . . . . . . 7 . . . . . . 
            . . . . 7 7 7 7 . 7 . . . . . . 
            . . . . . . . . 7 7 . . . . . . 
            . . . . . . . . . 7 . . . . . . 
            . . . . . . . . . 7 . . . . . . 
            . . . . . . . . . 7 . . . . . . 
            . . . . . . . . 7 . 7 . . . . . 
            . . . . . . . 7 . . . 7 . . . . 
            . . . . . . 7 . . . . . 7 . . .
    """),
    SpriteKind.enemy)
controller.move_sprite(Player1, 100, 100)
zombie.follow(Player1, 30)
difficulty = 1000
Player1.set_stay_in_screen(True)
zombie.set_position(0, 0)
Player1.set_position(75, 60)

def on_forever():
    global zombie
    pause(difficulty)
    zombie = sprites.create(img("""
            . . . . . . . 7 7 7 7 7 . . . . 
                    . . . . . . 7 7 7 7 7 7 7 . . . 
                    . . . . . . 7 7 2 7 7 7 7 . . . 
                    . . . . . . 7 7 2 7 7 7 7 . . . 
                    . . . . . . 7 7 7 7 7 7 7 . . . 
                    . . . . . . 2 2 7 7 7 7 7 . . . 
                    . . . . . . . 7 7 7 7 7 . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . 7 7 7 7 . 7 . . . . . . 
                    . . . . . . . . 7 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . . 7 . . . . . . 
                    . . . . . . . . 7 . 7 . . . . . 
                    . . . . . . . 7 . . . 7 . . . . 
                    . . . . . . 7 . . . . . 7 . . .
        """),
        SpriteKind.enemy)
    zombie.follow(Player1, 30)
    zombie.set_position(randint(5, scene.screen_width()),
        randint(5, scene.screen_height()))
forever(on_forever)

def on_forever2():
    global direction
    if controller.left.is_pressed():
        Player1.set_image(img("""
            . . . . . . . f f f f f . . . . 
                        . . . . . . f 1 1 1 1 1 f . . . 
                        . . . . . . f 1 8 1 1 1 f . . . 
                        . . . . . . f 1 8 1 1 1 f . . . 
                        . . . . . . f 1 1 1 1 1 f . . . 
                        . . . . . . f 8 8 1 1 1 f . . . 
                        . . b . . . . f f f f f . . . . 
                        . . b b b b b . . f . . . . . . 
                        . . . . b b b f . f . . . . . . 
                        . . . . . . b . f f . . . . . . 
                        . . . . . . b . . f . . . . . . 
                        . . . . . . . . . f . . . . . . 
                        . . . . . . . . . f . . . . . . 
                        . . . . . . . . f . f . . . . . 
                        . . . . . . . f . . . f . . . . 
                        . . . . . . f . . . . . f . . .
        """))
        direction = 0
    if controller.right.is_pressed():
        Player1.set_image(img("""
            . . . . f f f f f . . . . . . . 
                        . . . f 1 1 1 1 1 f . . . . . . 
                        . . . f 1 1 1 8 1 f . . . . . . 
                        . . . f 1 1 1 8 1 f . . . . . . 
                        . . . f 1 1 1 1 1 f . . . . . . 
                        . . . f 1 1 1 8 8 f . . . . . . 
                        . . . . f f f f f . . . . b . . 
                        . . . . . . f . . b b b b b . . 
                        . . . . . . f . f b b b . . . . 
                        . . . . . . f f . b . . . . . . 
                        . . . . . . f . . b . . . . . . 
                        . . . . . . f . . . . . . . . . 
                        . . . . . . f . . . . . . . . . 
                        . . . . . f . f . . . . . . . . 
                        . . . . f . . . f . . . . . . . 
                        . . . f . . . . . f . . . . . .
        """))
        direction = 1
forever(on_forever2)

def on_forever3():
    if info.life() == 0:
        game.over(False, effects.dissolve)
forever(on_forever3)

def on_forever4():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_melody("G C5 E B B E C5 G ", 1000)
    music.play_tone(466, music.beat(BeatFraction.WHOLE))
forever(on_forever4)

def on_forever5():
    global difficulty
    pause(2500)
    difficulty = difficulty - 10
forever(on_forever5)
