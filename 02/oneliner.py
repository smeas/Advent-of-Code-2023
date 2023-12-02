print(sum(
	map(
		lambda a:
			eval("*".join(map(
				str,
				map(
					lambda i: max(h[i] for h in a),
					[0,1,2])
			))),
		map(
			lambda l: [*map(
				lambda y: (
					lambda c,o: (o,*map(
						lambda s:
							(lambda v,n:
								o.__setitem__("rgb".index(n[0]), int(v))
							)(*s.split()),
							c.split(", ")
						)
					)[0]
				)(y,[0]*3),
				l.split(": ")[1].split("; ")
			)],
			open("i").readlines()
		)
	)
))

# 297 chars
print(sum(map(lambda a:eval("*".join(map(str,map(lambda i:max(h[i]for h in a),[0,1,2])))),map(lambda l:[*map(lambda y:(lambda c,o:(o,*map(lambda s:(lambda v,n:o.__setitem__("rgb".index(n[0]),int(v)))(*s.split()),c.split(", ")))[0])(y,[0]*3),l.split(": ")[1].split("; "))],open("i").readlines()))))