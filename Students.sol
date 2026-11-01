// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract StudentData{
    struct Student{
        uint rollNo;
        string name;
        uint age;
        string course;
    }

    Student public student;
    function setStudent(
        uint _rollNo,
        string memory _name,
        uint _age,
        string memory _course
    )public {
        student = Student(_rollNo, _name,_age,_course);

    }
    function getStudent() public view returns(
        uint,
        string memory,
        uint,
        string memory
    ){
        return (
            student.rollNo,
            student.name,
            student.age,
            student.course
        );
    }
}