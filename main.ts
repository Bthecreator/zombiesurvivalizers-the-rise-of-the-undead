controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (direction == 1) {
        bullet = sprites.createProjectileFromSprite(img`
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
            `, Player1, 300, 0)
    }
    if (direction == 0) {
        bullet = sprites.createProjectileFromSprite(img`
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
            `, Player1, -300, 0)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    pause(500)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    otherSprite2.destroy(effects.disintegrate, 500)
    info.changeScoreBy(10)
})
let bullet: Sprite = null
let direction = 0
let Player1: Sprite = null
scene.setBackgroundImage(img`
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
    `)
info.setLife(5)
Player1 = sprites.create(img`
    . . . . f f f f f . . . . . . . 
    . . . f . . . . . f . . . . . . 
    . . . f . . . f . f . . . . . . 
    . . . f . . . . . f . . . . . . 
    . . . f . . . . . f . . . . . . 
    . . . f . . . . . f . . . . . . 
    . . . . f f f f f . . . . . . . 
    . . . . . . f . . b b b b . . . 
    . . . . . . f . f b b . . . . . 
    . . . . . . f f . b . . . . . . 
    . . . . . . f . . . . . . . . . 
    . . . . . . f . . . . . . . . . 
    . . . . . . f . . . . . . . . . 
    . . . . . f . f . . . . . . . . 
    . . . . f . . . f . . . . . . . 
    . . . f . . . . . f . . . . . . 
    `, SpriteKind.Player)
let zombie = sprites.create(img`
    . . . . . . . 7 7 7 7 7 . . . . 
    . . . . . . 7 . . . . . 7 . . . 
    . . . . . . 7 . 2 . . . 7 . . . 
    . . . . . . 7 . . . . . 7 . . . 
    . . . . . . 7 . . . . . 7 . . . 
    . . . . . . 7 . . . . . 7 . . . 
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
    `, SpriteKind.Enemy)
controller.moveSprite(Player1, 100, 100)
zombie.follow(Player1, 30)
let difficulty = 1000
Player1.setStayInScreen(true)
zombie.setPosition(0, 0)
forever(function () {
    pause(difficulty)
    zombie = sprites.create(img`
        . . . . . . . 7 7 7 7 7 . . . . 
        . . . . . . 7 . . . . . 7 . . . 
        . . . . . . 7 . 2 . . . 7 . . . 
        . . . . . . 7 . . . . . 7 . . . 
        . . . . . . 7 . . . . . 7 . . . 
        . . . . . . 7 . . . . . 7 . . . 
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
        `, SpriteKind.Enemy)
    zombie.follow(Player1, 30)
    zombie.setPosition(randint(10, scene.screenWidth()), randint(10, scene.screenHeight()))
})
forever(function () {
    if (controller.left.isPressed()) {
        Player1.setImage(img`
            . . . . . . . f f f f f . . . . 
            . . . . . . f . . . . . f . . . 
            . . . . . . f . f . . . f . . . 
            . . . . . . f . . . . . f . . . 
            . . . . . . f . . . . . f . . . 
            . . . . . . f . . . . . f . . . 
            . . . . . . . f f f f f . . . . 
            . . . b b b b . . f . . . . . . 
            . . . . . b b f . f . . . . . . 
            . . . . . . b . f f . . . . . . 
            . . . . . . . . . f . . . . . . 
            . . . . . . . . . f . . . . . . 
            . . . . . . . . . f . . . . . . 
            . . . . . . . . f . f . . . . . 
            . . . . . . . f . . . f . . . . 
            . . . . . . f . . . . . f . . . 
            `)
        direction = 0
    }
    if (controller.right.isPressed()) {
        Player1.setImage(img`
            . . . . f f f f f . . . . . . . 
            . . . f . . . . . f . . . . . . 
            . . . f . . . f . f . . . . . . 
            . . . f . . . . . f . . . . . . 
            . . . f . . . . . f . . . . . . 
            . . . f . . . . . f . . . . . . 
            . . . . f f f f f . . . . . . . 
            . . . . . . f . . b b b b . . . 
            . . . . . . f . f b b . . . . . 
            . . . . . . f f . b . . . . . . 
            . . . . . . f . . . . . . . . . 
            . . . . . . f . . . . . . . . . 
            . . . . . . f . . . . . . . . . 
            . . . . . f . f . . . . . . . . 
            . . . . f . . . f . . . . . . . 
            . . . f . . . . . f . . . . . . 
            `)
        direction = 1
    }
})
forever(function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
    music.playMelody("G C5 E B B E C5 G ", 1000)
    music.playTone(466, music.beat(BeatFraction.Whole))
})
forever(function () {
    pause(2500)
    difficulty = difficulty - 10
})
forever(function () {
    if (info.life() == 0) {
        game.over(false)
    }
})
