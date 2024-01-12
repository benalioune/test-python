import pytest

#Functions to test

def total_with_tip(bill, percentage):
    if bill < 0:
        raise ValueError("Bill cannot be negative")
    if percentage > 100:
        raise ValueError("Percentage cannot be greater than 100%")
    if percentage < 0:
        raise ValueError("Percentage cannot be negative")
    
    tip = bill * percentage / 100
    if tip > 500:
        tip = 500
    
    total = bill + tip
    if total < 5:
        total = 5
    return round(total, 2)



# TDD - Test Driven Development
# 1. Pour un repas à *100€* (bill), et un tips de *20%*(percentage) : Je laisse sur la table *120€*(output/return).
def test_tip_classic():
    assert total_with_tip(100, 20) == 120

def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100

# Exercice : écrire les tests correspondants : 
# 2. Le tip maximal est de 500€ car il n'existe pas de billet plus gros.
def test_tip_max():
    assert total_with_tip(1000, 51)== 1500
    assert total_with_tip(5000, 15)== 5500
    assert total_with_tip(2000, 26)== 2500
    assert total_with_tip(10000, 12)== 10500

    
# 3. Le plus petit billet étant 5€, il n'est pas possible d'avoir un total plus bas de 5€
def test_min_total():
    assert total_with_tip(1,0) == 5
    assert total_with_tip(2.30,20) == 5
    assert total_with_tip(4,15) == 5
    assert total_with_tip(3,50) == 5

# 4. Vérifer que l'arrondie du total est bien sur deux décimales
def test_two_decimals():
    assert total_with_tip(5, 12.45) == 5.62
    assert total_with_tip(10.12,15) == 11.64
    assert total_with_tip(10, 2.33) == 10.23
    

# 5. Adater votre function d'implementation pour passer les tests

# TODO:Tester les pourcentages -> Exception 
def test_error_percentage():
    with pytest.raises(ValueError):
        total_with_tip(100, 101)
    with pytest.raises(ValueError):
        total_with_tip(100, -1)

def test_error_bill():
    with pytest.raises(ValueError):
        total_with_tip(-100, 20)
    with pytest.raises(ValueError):
        total_with_tip(-100, 0)