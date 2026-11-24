# Tiny Chess Engine

A complete chess engine in 4,093 bytes of Python. One file, stdlib only.

## What it is

Built as an entry for the make.fun bounty **tiny-chess-01** — "Build the strongest chess engine in 4 KB of Python" (competition entry project, not a commercial product).

Full rules: castling, en passant, promotion, check, checkmate and stalemate. Negamax alpha-beta search with iterative deepening, a transposition table, quiescence search and check extensions, on a 0x88 board. Fixed 50,000-node budget per move, so it is fully deterministic: the same position always gets the same move.

## Run it

```sh
python3 -P -s main.py
```

It plays through the make.fun environment server (`MAKEFUN_ENV_URL`): `POST /game`, `POST /move`, `POST /resign`.

## Results

- Practice trial (official env + scorer): Elo 1,191, above the 1,154 entry floor.
- Perft verified: start position depth 3 = 8,902; Kiwipete depth 2 = 2,039; en-passant position depth 3 = 2,812.
- See it play: a full 93-move self-play game, Black winning by checkmate, was recorded with this engine on both sides.

## License

MIT
