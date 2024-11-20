from datetime import datetime
from collections import namedtuple

class BTreeNode:
    def __init__(self, t):
        self.t = t  # Mínimo grado del B-tree
        self.keys = []  # Claves en el nodo
        self.children = []  # Hijos del nodo
        self.is_leaf = True  # Indica si es hoja

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i].url:
            i += 1

        if i < len(node.keys) and key == node.keys[i].url:
            return node.keys[i]

        if node.is_leaf:
            return None

        return self.search(node.children[i], key)

    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BTreeNode(t)
        new_child.is_leaf = child.is_leaf
        parent.children.insert(index + 1, new_child)
        parent.keys.insert(index, child.keys[t - 1])

        new_child.keys = child.keys[t:]
        child.keys = child.keys[:t - 1]

        if not child.is_leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.is_leaf:
            while i >= 0 and key.url < node.keys[i].url:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            while i >= 0 and key.url < node.keys[i].url:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)

                if key.url > node.keys[i].url:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t)
            new_root.is_leaf = False
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

class Cache:
    CacheEntry = namedtuple('CacheEntry', ['url', 'content', 'timestamp'])

    def __init__(self, btree_order=3):
        self.btree = BTree(btree_order)

    def agregar_cache(self, url, content):
        timestamp = datetime.now()
        entry = self.CacheEntry(url, content, timestamp)
        self.btree.insert(entry)

    def obtener_cache(self, url):
        result = self.btree.search(self.btree.root, url)
        if result:
            print(f"Contenido en caché para {url}: {result.content}")
        else:
            print(f"No se encontró contenido en caché para {url}.")

    def vaciar_cache(self, url=None, fecha=None):
        if url:
            print(f"Eliminando caché para URL: {url}")
            # Implementación específica para eliminar por URL
        elif fecha:
            print(f"Eliminando caché posterior a: {fecha}")
            # Implementación específica para eliminar por fecha
        else:
            print("Debe proporcionar un parámetro válido (--url o --fecha).")


"""
# Ejemplo de uso
if __name__ == "__main__":
    cache = Cache()
    cache.agregar_cache("www.ejemplo.com", "<html>Contenido de Ejemplo</html>")
    cache.obtener_cache("www.ejemplo.com")
    cache.vaciar_cache(url="www.ejemplo.com")
"""