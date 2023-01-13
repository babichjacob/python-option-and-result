from option_and_result import NONE, Some, Ok, Err


def test_readme_part_1():
    maybe_a_number = Some(17)
    assert maybe_a_number.unwrap() == 17


def test_readme_part_2():
    nothing = NONE()
    assert nothing.is_none()


def test_readme_part_3():
    maybe_a_number = Some(17)
    number_result = maybe_a_number.ok_or("not a number")
    assert number_result == Ok(17)


def test_readme_part_4():
    number_result = Ok(17)
    result_that_is_err = Err("gah! an error!")
    combinatoric_result = number_result.and_(result_that_is_err)

    assert combinatoric_result.unwrap_err() == "gah! an error!"
