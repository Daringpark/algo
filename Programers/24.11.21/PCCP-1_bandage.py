def solution(bandage, health, attacks):
    # bandage = t, x, y
    # attacks = T, P
    band_time, heal_by_band, heal_by_comp = bandage
    
    current_health, max_health = health, health
    current_time = 0
    heal_flag = 0
    heal_count, extra_heal = 0, 0
    
    time = attacks[-1][0]
    # 제일 처음에는?
    for attack in attacks:
        T, P = attack
        spent_time = T-current_time-1
        heal_count, extra_heal = 0, 0
        
        # point for healing
        if heal_flag and spent_time > 0:
            heal_count, extra_heal = spent_time * heal_by_band, (spent_time//band_time) * heal_by_comp 
        
        # Heal First
        current_health += heal_count + extra_heal
        if max_health < current_health:
            current_health = max_health
        
        # Being Attacked
        current_health -= P
        
        # Result
        current_time = T
        heal_flag = 1

        if current_health <= 0:
            return -1
    
    return current_health