/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr)
            return nullptr;

        Node* head = new Node(node->val);
        Node* f = head;

        std::deque<Node*> queue = {};
        queue.push_back(node);

        std::unordered_map<int, Node*> seenNodes = {};
        seenNodes[f->val] = f;

        while (queue.size() != 0) {
            Node* cur = queue.front();
            queue.pop_front();

            Node* copyCur = seenNodes.at(cur->val);

            for (Node* nbr : cur->neighbors) {
                if (seenNodes.contains(nbr->val)) {
                    copyCur->neighbors.push_back(seenNodes[nbr->val]);
                } else {
                    queue.push_back(nbr);

                    Node* copy = new Node(nbr->val);
                    seenNodes[nbr->val] = copy;
                    copyCur->neighbors.push_back(copy);
                }
            }
        }

        return head;
    }
};