# Bill Splitter

## Description

A command line interface (CLI) app that gets as input the amount of a `bill` for a particular `payment cycle` and the days each `person` `stayed` in the house during the payment cycle. Then return the amount each has to `pay`. It also generates a `PDF` report stating the names of each person, the payment period, and how much each has to pay.

## Design Plan

Objects:

- Bill: amount, period
- Person: name, days_in_house, pays(bill)
- PdfReport: filename, generate(person1, person2, bill)
