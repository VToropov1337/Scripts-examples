from collections import namedtuple

Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)



def test_type_of_values():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': str,
                'owner': str,
                'done': bool,
                'id': int}
    for k in t_dict.keys():
        assert type(t_dict[k]) == expected[k]