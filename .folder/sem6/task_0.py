"""
values = [True, False, True, None, True]
result = []
for v in values:
    if v is True:
        result.appent('yes')
    else:
        if v is False:
            result.append('no')
        else:
            result.append('unknown')

print(result)
"""

values = [True, False, True, None, True]
print(['yes' if v is True else 'no' if v is False else "unknown" for v in values])