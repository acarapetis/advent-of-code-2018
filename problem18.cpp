#include <list>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <algorithm>

// Who needs maths when you can just go fast instead
template<typename T>
typename std::list<T>::iterator circularNext(std::list<T> &l, typename std::list<T>::iterator it) {
    return std::next(it) == l.end() ? l.begin() : std::next(it);
}
template<typename T>
typename std::list<T>::iterator circularNext(std::list<T> &l, typename std::list<T>::iterator it, size_t c) {
    while (c--) it = circularNext(l, it);
    return it;
}

template<typename T>
typename std::list<T>::iterator circularPrev(std::list<T> &l, typename std::list<T>::iterator it) {
    return std::prev(it == l.begin() ? l.end() : it);
}
template<typename T>
typename std::list<T>::iterator circularPrev(std::list<T> &l, typename std::list<T>::iterator it, size_t c) {
    while (c--) it = circularPrev(l, it);
    return it;
}

int main(int argc, char** argv) {
    long playerCount;
    long maxMarble;
    if (scanf("%ld players; last marble is worth %ld points", &playerCount, &maxMarble) != 2) {
        std::cerr << "Unexpected input format." << std::endl;
        return 1;
    }
    if (playerCount <= 0 || maxMarble <= 0) {
        std::cerr << "Player count and max marble must both be positive ints." << std::endl;
        return 2;
    }
    maxMarble *= 100;

    std::list<long> circle { 0 };
    std::vector<long> scores(playerCount, 0);

    auto current = circle.begin();
    long player = 0;
    for (long marble = 1; marble <= maxMarble; marble++) {
        player = (player + 1) % playerCount;

        if (marble % 23 == 0) {
            current = circularPrev(circle, current, 7);
            scores[player] += *current + marble;
            current = circle.erase(current);
        } else {
            current = circle.insert(circularNext(circle, current, 2), marble);
        }
    }
    auto max = *std::max_element(scores.begin(), scores.end());
    std::cout << max << std::endl;

    return 0;
}
