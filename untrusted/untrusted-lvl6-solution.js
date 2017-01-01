
/****************
 * drones101.js *
 ****************
 *
 * Do you remember, my dear Professor, a certain introductory
 * computational rationality class you taught long ago? Assignment
 * #2, behavior functions of autonomous agents? I remember that one
 * fondly - but attack drones are so much easier to reason about
 * when they're not staring you in the face, I would imagine!
 */

function startLevel(map) {
    function moveToward(obj, type) {
        var target = obj.findNearest(type);
        var leftDist = obj.getX() - target.x;
        var upDist = obj.getY() - target.y;

        var direction;
        if (upDist == 0 && leftDist == 0) {
            return;
        } if (upDist > 0 && upDist >= leftDist) {
            direction = 'up';
        } else if (upDist < 0 && upDist < leftDist) {
            direction = 'down';
        } else if (leftDist > 0 && leftDist >= upDist) {
            direction = 'left';
        } else {
            direction = 'right';
        }

        if (obj.canMove(direction)) {
            obj.move(direction);
        }
    }

    map.defineObject('attackDrone', {
        'type': 'dynamic',
        'symbol': 'd',
        'color': 'red',
        'onCollision': function (player) {
            player.killedBy('an attack drone');
        },
        'behavior': function (me) {
            moveToward(me, 'player');
        }
    });


    map.placePlayer(1, 1);
    map.placeObject(map.getWidth()-2, 12, 'attackDrone');
    map.placeObject(map.getWidth()-1, 12, 'exit');

    map.placeObject(map.getWidth()-1, 11, 'block');
    map.placeObject(map.getWidth()-2, 11, 'block');
    map.placeObject(map.getWidth()-1, 13, 'block');
    map.placeObject(map.getWidth()-2, 13, 'block');
    
    //----------------------------------------------------------------------

    // Drone's path if you just go directly right
    for (x = 2; x <= 20; ++x)
    {
        map.setSquareColor(map.getWidth()-x, 12, "darkred")
    }
    for (y = 12; y >= 1; --y)
    {
        map.setSquareColor(map.getWidth()-20, y, "darkred")
    }
    
    // can we block the thing? 
    map.placeObject(map.getWidth()-19, 9, "block")
    map.placeObject(map.getWidth()-19, 10, "block")
    map.placeObject(map.getWidth()-20, 9, "block")
    map.placeObject(map.getWidth()-21, 9, "block")
    map.placeObject(map.getWidth()-21, 10, "block")
    
    // we can. Solution path.
    for (x = 1; x <= 47; ++x)
    {
        map.setSquareColor(x, 1, "darkgreen")
    }
    for (y = 1; y <= 12; ++y)
    {
        map.setSquareColor(47, y, "darkgreen")
    }
    
    //----------------------------------------------------------------------

}

function validateLevel(map) {
    map.validateExactlyXManyObjects(1, 'exit');
}
