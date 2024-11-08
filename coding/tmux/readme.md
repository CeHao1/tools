

## create session
```
tmux new -s my_session_name
```

```
tmux # will create session with numbered index [0] [1],...
```

## check all session
```
tmux ls
```

## enter session
```
tmux attach -t [session name or index]
```

## exit session
```
ctrl+B, D
```

## kill session
```
tmux kill-session -t my_session_name
```

or in the session terminal
```
ctrl+D
```

